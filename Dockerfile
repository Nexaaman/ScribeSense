FROM python:3.10

WORKDIR /app

COPY . /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt



EXPOSE 8000 8501

CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port 8000 & streamlit run app_fron-end.py --server.port 8501 --server.address 0.0.0.0"]


