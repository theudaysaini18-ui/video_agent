import os
import httpx
from config import settings


async def transcribe_with_sarvam(audio_path: str, language: str = "hi") -> str:
    """
    Transcribes Hindi/Hinglish audio using Sarvam AI.
    This is a placeholder assuming a typical REST API:
      - POST /transcribe
      - body: { "audio": base64, "language": "hi" }
      - header: Authorization: Bearer <SARVAM_API_KEY>
      - response: { "transcript": "..." }

    Adjust according to actual Sarvam API docs when available.
    """
    if not settings.sarvam_api_key:
        raise RuntimeError("SARVAM_API_KEY not set in .env")

    # Read audio as bytes and base64-encode
    import base64
    with open(audio_path, "rb") as f:
        audio_bytes = f.read()
    audio_b64 = base64.b64encode(audio_bytes).decode("ascii")

    url = f"{settings.sarvam_base_url}/transcribe"
    headers = {
        "Authorization": f"Bearer {settings.sarvam_api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "audio": audio_b64,
        "language": language,  # e.g. "hi" for Hindi/Hinglish
    }

    async with httpx.AsyncClient(timeout=120.0) as client:
        resp = await client.post(url, json=payload, headers=headers)
        resp.raise_for_status()
        data = resp.json()

    # Adapt key names as per real API
    transcript = data.get("transcript") or data.get("text") or ""
    if not transcript:
        raise RuntimeError("Sarvam response did not contain transcript")

    return transcript.strip()