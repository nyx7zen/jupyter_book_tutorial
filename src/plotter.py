import matplotlib.pyplot as plt
import numpy as np


def plot_signal(x: np.ndarray, y: np.ndarray, title: str = "Signal"):
    """단일 신호 플롯

    Args:
        x: 시간축 배열
        y: 신호 배열
        title: 그래프 제목
    """
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.plot(x, y, color="steelblue", linewidth=1.5)
    ax.set_title(title)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    ax.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()


def plot_multiple(x: np.ndarray, signals: list, labels: list,
                  title: str = "Signals"):
    """여러 신호 비교 플롯

    Args:
        x: 시간축 배열
        signals: 신호 배열 리스트
        labels: 각 신호의 레이블 리스트
        title: 그래프 제목
    """
    fig, ax = plt.subplots(figsize=(8, 3))
    colors = ["steelblue", "tomato", "seagreen", "orange"]
    for i, (y, label) in enumerate(zip(signals, labels)):
        ax.plot(x, y, label=label, color=colors[i % len(colors)], linewidth=1.5)
    ax.set_title(title)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()


def plot_with_noise(x: np.ndarray, y_clean: np.ndarray, y_noisy: np.ndarray,
                    title: str = "Signal with Noise"):
    """원본 신호 vs 노이즈 추가 신호 비교 플롯

    Args:
        x: 시간축 배열
        y_clean: 원본 신호 배열
        y_noisy: 노이즈 추가 신호 배열
        title: 그래프 제목
    """
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.plot(x, y_noisy, color="tomato", linewidth=1.0, alpha=0.7, label="Noisy")
    ax.plot(x, y_clean, color="steelblue", linewidth=2.0, label="Clean")
    ax.set_title(title)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()
