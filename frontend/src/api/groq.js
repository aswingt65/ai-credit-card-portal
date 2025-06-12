// src/api/groq.js
export async function fetchInsightsFromGroq(prompt) {
  const response = await fetch("https://api.groq.com/v1/chat/completions", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${import.meta.env.GROQ_API_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      model: "mixtral-8x7b-32768", // or other Groq model
      messages: [
        {
          role: "system",
          content: "You are a financial assistant analyzing credit card transactions.",
        },
        {
          role: "user",
          content: prompt,
        },
      ],
    }),
  });

  const data = await response.json();
  return data.choices?.[0]?.message?.content || "No insights available.";
}
