"use client";
import { useState, useRef, useEffect } from 'react';
import Image from 'next/image';
import type { Message, APIResponse } from '@/types';
import styles from '@/styles/HealthChat.module.css';

export default function HealthChat() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [hasMounted, setHasMounted] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  // Fix hydration by waiting for mount
  useEffect(() => {
    setHasMounted(true);
    messagesEndRef.current?.scrollIntoView();
  }, []);

  // Auto-scroll when messages update
  useEffect(() => {
    if (hasMounted) {
      messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    }
  }, [messages, hasMounted]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim() || isLoading) return;

    setIsLoading(true);
    setMessages(prev => [...prev, { text: input, sender: 'user' }]);

    try {
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_input: input }),
      });

      if (!response.ok) throw new Error(`Something went wrong. Please try again (check API key or server), Error: ${response.status}`);
      
      const data: APIResponse = await response.json();
      setMessages(prev => [...prev, {
        text: data.response,
        sender: 'bot',
        source: data.source,
        tokensUsed: data.tokens_used
      }]);
    } catch (error) {
      console.error('API Error:', error);
      setMessages(prev => [...prev, {
        text: error instanceof Error
          ? `⚠️ ${error.message}`
          : "⚠️ Something went wrong. Please try again (check API key or server).",
        sender: 'bot'
      }]);
    } finally {
      setIsLoading(false);
      setInput('');
    }
  };

  // Prevent hydration mismatch
  if (!hasMounted) return (
    <div className={styles.container}>
      <header className={styles.header}>
        <h1>🌿 Health & Wellness Assistant</h1>
      </header>
      <div className={styles.chatContainer}>
        <p>Loading...</p>
      </div>
    </div>
  );

  return (
    <div className={styles.container} suppressHydrationWarning>
      <header className={styles.header}>
        <h1>🌿 Health & Wellness Assistant</h1>
        <p>Ask me anything about fitness, nutrition, or general health!</p>
      </header>

      <div className={styles.chatContainer}>
        {messages.length === 0 ? (
          <div className={styles.welcomeMessage}>
            <Image
              src="/h2.png"
              alt="Health Bot"
              width={100}
              height={100}
              priority
            />
            <p>Hi there! I can help with:</p>
            <ul>
              <li>Weight loss plans</li>
              <li>Exercise techniques</li>
              <li>Healthy recipes</li>
              <li>General wellness tips</li>
            </ul>
          </div>
        ) : (
          messages.map((msg, i) => (
            <div
              key={i}
              className={`${styles.message} ${
                msg.sender === 'user' ? styles.userMessage : styles.botMessage
              }`}
            >
              {msg.sender === 'bot' && <div className={styles.botIndicator}>🤖</div>}
              <div className={styles.messageContent}>
                <p>{msg.text}</p>
                {msg.source && (
                  <div className={styles.messageMeta}>
                    <span className={
                      msg.source === 'local' ? styles.localTag : styles.openaiTag
                    }>
                      {msg.source === 'local' ? 'Local Knowledge' : 'AI Generated'}
                    </span>
                    {msg.tokensUsed && (
                      <span className={styles.tokenBadge}>
                        {msg.tokensUsed} tokens
                      </span>
                    )}
                  </div>
                )}
              </div>
            </div>
          ))
        )}
        {isLoading && (
          <div className={styles.typingIndicator}>
            <span>•</span>
            <span>•</span>
            <span>•</span>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      <form onSubmit={handleSubmit} className={styles.inputForm}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask about health..."
          className={styles.inputField}
          disabled={isLoading}
          aria-label="Type your health question"
        />
        <button
          type="submit"
          className={styles.sendButton}
          disabled={isLoading || !input.trim()}
          aria-label="Send message"
        >
          {isLoading ? 'Sending...' : 'Send'}
        </button>
      </form>
      <footer className={styles.footer}>
      <p>✍️ Author:  <strong>Azmat Ali Akbar</strong></p>
    </footer>
    </div>
  );
}