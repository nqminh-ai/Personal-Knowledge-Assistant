"""Run one guarded LLM smoke test using OpenAI or Gemini credentials."""

from __future__ import annotations

import os
import sys
import time

from dotenv import load_dotenv


def main() -> int:
    load_dotenv()
    question = "Theo CONTEXT, hệ thống cần làm gì khi không có đủ bằng chứng?"
    context = "Nếu không tìm thấy đủ bằng chứng trong tài liệu, trợ lý phải nói rõ rằng chưa đủ thông tin."
    prompt = (
        "Answer in Vietnamese using only CONTEXT. Be concise. "
        "If the answer is unsupported, abstain.\n\n"
        f"CONTEXT:\n{context}\n\nQUESTION:\n{question}"
    )

    started = time.perf_counter()
    if os.getenv("OPENAI_API_KEY"):
        try:
            from openai import OpenAI
        except ImportError:
            print("Missing dependency: openai")
            return 2
        client = OpenAI()
        response = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
        )
        answer = response.choices[0].message.content or ""
        provider = "OpenAI"
    elif os.getenv("GEMINI_API_KEY"):
        try:
            from google import genai
        except ImportError:
            print("Missing dependency: google-genai")
            return 2
        client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
        response = client.models.generate_content(
            model=os.getenv("GEMINI_MODEL", "gemini-2.0-flash"),
            contents=prompt,
        )
        answer = response.text or ""
        provider = "Gemini"
    else:
        print("SKIP: set OPENAI_API_KEY or GEMINI_API_KEY in .env to run the API test")
        return 0

    elapsed_ms = (time.perf_counter() - started) * 1000
    print(f"Provider: {provider}")
    print(f"Latency: {elapsed_ms:.0f} ms")
    print(f"Answer: {answer.strip()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
