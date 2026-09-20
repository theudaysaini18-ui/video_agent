from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Mistral
    mistral_api_key: str

    # Sarvam
    sarvam_api_key: str = ""
    sarvam_base_url: str = "https://api.sarvam.ai"

    # Whisper
    whisper_model: str = "base"  # tiny, base, small, medium, large-v3

    # Embeddings
    embedding_model: str = "all-MiniLM-L6-v2"

    # Chroma
    chroma_persist_dir: str = "./chroma_db"

    # yt-dlp / audio
    audio_dir: str = "./audio_cache"
    output_dir: str = "./outputs"

    class Config:
        env_file = ".env"


settings = Settings()