from faster_whisper import WhisperModel

from config import settings


def transcribe_with_whisper(audio_path: str, language: str = "en") -> str:
    """
    Transcribes audio using local faster-whisper.
    Returns full transcript as a single string.
    """
    model_size = settings.whisper_model
    device = "cuda"  # if you have GPU; else use "cpu"
    # If CUDA not available, fallback to "cpu"
    try:
        model = WhisperModel(model_size, device=device, compute_type="float32")
    except Exception:
        model = WhisperModel(model_size, device="cpu", compute_type="int8")

    segments, _ = model.transcribe(audio_path, language=language)
    transcript_parts = [seg.text for seg in segments]
    return " ".join(transcript_parts).strip()