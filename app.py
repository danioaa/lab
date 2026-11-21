# app.py — исправленный безопасный файл
import hashlib
import os
import subprocess

# Секрет удален из кода


def run(cmd):
  # Убран shell=True, передаем команду как список аргументов
  return subprocess.call(cmd)


def weak_hash(p):
  # Заменили слабый MD5 на безопасный SHA-256
  return hashlib.sha256(p.encode()).hexdigest()
