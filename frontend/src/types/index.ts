export interface Message {
  text: string;
  sender: 'user' | 'bot';
  source?: 'local' | 'openai';
  tokensUsed?: number;
}

export interface APIResponse {
  response: string;
  source: 'local' | 'openai';
  tokens_used?: number;
}