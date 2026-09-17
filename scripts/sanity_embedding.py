"""Run a small local embedding smoke test for Vietnamese text."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def main() -> int:
    try:
        from sentence_transformers import SentenceTransformer
    except ImportError:
        print("Missing dependency. Run: pip install -r requirements.txt")
        return 2

    model_name = "BAAI/bge-m3"
    texts = [
        "Mạng nơ-ron học các biểu diễn từ dữ liệu huấn luyện.",
        "Đánh giá mô hình cần tập kiểm thử độc lập.",
        "Retrieval tìm các đoạn tài liệu liên quan đến câu hỏi.",
        "BM25 phù hợp với truy vấn chứa từ khóa chính xác.",
        "RAG sử dụng ngữ cảnh truy xuất để tạo câu trả lời.",
    ]

    print(f"Loading {model_name} ...")
    model = SentenceTransformer(model_name)
    embeddings = model.encode(texts, normalize_embeddings=True, show_progress_bar=False)

    if len(embeddings) != len(texts) or embeddings.shape[1] == 0:
        print("FAIL: unexpected embedding shape")
        return 1

    print(f"PASS: encoded {len(texts)} texts; shape={embeddings.shape}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
