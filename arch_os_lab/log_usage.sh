#!/bin/bash

# Параметры
LOG_DIR="/LOG"
BACKUP_DIR="/BACKUP"
THRESHOLD=70      # Порог использования в процентах
FILE_COUNT=10     # Количество файлов для архивации
MAX_SIZE_MB=1024   # Максимальный размер папки /LOG в МБ

# Функция для конвертации размера в Мегабайты
convert_to_mb() {
  echo "$1 / 1024" | bc
}

# Вычисляем текущий размер папки /LOG в МБ
current_size_kb=$(du -s "$LOG_DIR" | awk '{print $1}')
current_size_mb=$(convert_to_mb "$current_size_kb")

echo "Текущий размер папки $LOG_DIR: $current_size_mb МБ"

# Вычисляем процент заполнения относительно MAX_SIZE_MB
current_usage=$(echo "$current_size_mb * 100 / $MAX_SIZE_MB" | bc)

echo "Заполненность папки $LOG_DIR: $current_usage%"

# Если использование больше порога
if [ "$current_usage" -ge "$THRESHOLD" ]; then
  echo "Использование $LOG_DIR превышает $THRESHOLD%, архивируем файлы..."

  # Создаём backup с текущей датой
  timestamp=$(date +"%Y%m%d_%H%M%S")
  backup_file="$BACKUP_DIR/backup_$timestamp.tar.gz"

  # Получаем список N последних файлов по дате модификации
  files_to_archive=$(ls -t "$LOG_DIR" | head -n $FILE_COUNT)

  # Архивируем выбранные файлы
  tar -czf "$backup_file" -C "$LOG_DIR" $files_to_archive

  echo "Файлы заархивированы в $backup_file"

  # Удаляем заархивированные файлы из папки /LOG
  for file in $files_to_archive; do
    rm "$LOG_DIR/$file"
    echo "Файл $file удалён из $LOG_DIR"
  done
else
  echo "Использование $LOG_DIR в норме."
fi