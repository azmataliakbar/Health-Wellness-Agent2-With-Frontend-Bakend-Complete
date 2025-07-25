import type { NextApiRequest, NextApiResponse } from 'next';

type APIResponse = {
  response: string;
  source: 'local' | 'openai';
  tokens_used?: number;
};

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<APIResponse>
) {
  if (req.method !== 'POST') {
    res.setHeader('Allow', ['POST']);
    return res.status(405).end(`Method ${req.method} Not Allowed`);
  }

  try {
    const { user_input } = req.body;

    if (!user_input || typeof user_input !== 'string') {
      throw new Error('Invalid input: user_input must be a string');
    }

    // Call FastAPI with user_input as a URL-encoded query parameter
    const fastApiUrl = `${process.env.NEXT_PUBLIC_BACKEND_URL}/query?user_input=${encodeURIComponent(user_input)}`;
    const fastApiResponse = await fetch(fastApiUrl, {
      method: 'POST',
      headers: { 'Accept': 'application/json' },
    });

    if (!fastApiResponse.ok) {
      const errorText = await fastApiResponse.text();
      throw new Error(`FastAPI error: ${errorText}`);
    }

    const data = await fastApiResponse.json();

    // Validate response structure
    if (!data.response || !data.source) {
      throw new Error('Invalid response from FastAPI');
    }

    return res.status(200).json({
      response: data.response,
      source: data.source,
      tokens_used: data.tokens_used,
    });

  } catch (error) {
    console.error('API Error:', error);
    return res.status(500).json({
      response: `Error: ${error instanceof Error ? error.message : 'Request failed'}`,
      source: 'local',
      tokens_used: 0,
    });
  }
}