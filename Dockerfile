FROM python:3.7

WORKDIR /src
COPY requirements.txt ./
COPY src ./
COPY tests ./
RUN pip3 install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y vim

COPY . .
EXPOSE 3000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "3000" , "--reload"]
