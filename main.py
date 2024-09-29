import sys
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

BOT_SCRIPT = 'tgBot.py'


class ReloadBotHandler(FileSystemEventHandler):
  def __init__(self):
    self.process = None
    self.start_bot()

  def start_bot(self):
    if self.process:
      self.process.kill()
    print("Запуск бота...")
    self.process = subprocess.Popen([sys.executable, BOT_SCRIPT])

  def on_modified(self, event):
    if event.src_path.endswith('.py'):
      print(f"Файл {event.src_path} змінений. Перезавантаження бота...")
      self.start_bot()


if __name__ == "__main__":
  path = '.'
  event_handler = ReloadBotHandler()
  observer = Observer()
  observer.schedule(event_handler, path, recursive=True)

  print("Система спостереження запущена. Стежимо за змінами в файлах...")
  observer.start()

  try:
    while True:
      time.sleep(1)
  except KeyboardInterrupt:
    observer.stop()
  observer.join()
