import os


class Settings:
    SERVER_PORT: int = int(os.getenv("SERVER_PORT", "8080"))
    APP_NAME: str = os.getenv("APP_NAME", "llm-spring-ai")
    OLLAMA_BASE_URL: str = os.getenv("OLLAMA_BASE_URL", "https://ollama.com")
    OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "gemma4:31b")
    
    OLLAMA_TEMPERATURE: float = float(os.getenv("OLLAMA_TEMPERATURE", "0.7"))
    OLLAMA_API_KEY: str = os.getenv("OLLAMA_API_KEY", "e8568dd48bfc42409069f9de96e2508e.Nl9CHJ2YZK-Hl-6HyBtkx0AL")


settings = Settings()
