# video-search

A searchable archive of long-form technical talks. Keyword and semantic search across timestamped transcripts, with deep links into the source video.

## What it does

- Transcribes uploaded talks using self-hosted Whisper, producing word-level timestamps and WebVTT subtitle files
- Generates embeddings for every transcript chunk, enabling semantic search — "how to scale databases" matches talks about sharding even without the literal word
- RAG-based Q&A: ask natural-language questions and get cited answers across the corpus
- Click any search result to jump to the exact moment in the source video

## Tech stack

- **Frontend**: Next.js + TypeScript + Tailwind
- **Backend**: FastAPI (Python)
- **Database**: Postgres + pgvector
- **Async pipeline**: Celery + Redis
- **Transcription**: faster-whisper (self-hosted)
- **Embeddings**: BGE small (sentence-transformers)
- **LLM (RAG)**: Google Gemini Flash
- **Storage**: MinIO locally, Cloudflare R2 in production

## Status

🚧 In development.
