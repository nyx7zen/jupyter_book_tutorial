import numpy as np


def generate_sine(freq: float = 1.0, samples: int = 200, duration: float = 1.0):
    """사인파 생성

    Args:
        freq: 주파수 (Hz)
        samples: 샘플 수
        duration: 시간 길이 (초)

    Returns:
        x: 시간축 배열
        y: 사인파 배열
    """
    x = np.linspace(0, duration, samples)
    y = np.sin(2 * np.pi * freq * x)
    return x, y


def generate_cosine(freq: float = 1.0, samples: int = 200, duration: float = 1.0):
    """코사인파 생성

    Args:
        freq: 주파수 (Hz)
        samples: 샘플 수
        duration: 시간 길이 (초)

    Returns:
        x: 시간축 배열
        y: 코사인파 배열
    """
    x = np.linspace(0, duration, samples)
    y = np.cos(2 * np.pi * freq * x)
    return x, y


def add_noise(y: np.ndarray, std: float = 0.1):
    """가우시안 노이즈 추가

    Args:
        y: 입력 신호 배열
        std: 노이즈 표준편차

    Returns:
        y_noisy: 노이즈가 추가된 신호 배열
    """
    noise = np.random.normal(0, std, size=y.shape)
    return y + noise


def generate_composite(freq1: float = 1.0, freq2: float = 3.0,
                        samples: int = 200, duration: float = 1.0):
    """사인파 + 코사인파 합성파 생성

    Args:
        freq1: 사인파 주파수 (Hz)
        freq2: 코사인파 주파수 (Hz)
        samples: 샘플 수
        duration: 시간 길이 (초)

    Returns:
        x: 시간축 배열
        y: 합성파 배열
    """
    x = np.linspace(0, duration, samples)
    y = np.sin(2 * np.pi * freq1 * x) + np.cos(2 * np.pi * freq2 * x)
    return x, y
