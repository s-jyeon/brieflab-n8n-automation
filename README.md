# 📬 Gemini 뉴스 요약 자동화 시스템 (n8n + FastAPI)

**Gemini + LangChain 기반 뉴스 요약 자동화 시스템**  
사용자 관심사에 맞는 뉴스를 요약하고, 이메일로 발송하는 전체 파이프라인을 n8n과 FastAPI로 구성했습니다.

---

## 📁 프로젝트 구조

<pre>
.
├── Dockerfile                  # FastAPI 애플리케이션용 Dockerfile
├── app.py                      # FastAPI 서버 진입점
├── docker-compose.yml          # 전체 서비스 정의
├── requirements.txt            # Python 의존성 목록
├── n8n/                        # n8n 관련 리소스
│   ├── Dockerfile              # n8n용 커스텀 Dockerfile
│   ├── diagram/                # 프로젝트 구조 및 워크플로우 다이어그램
│   ├── examples/               # 이메일 HTML 샘플 등 예제
│   └── workflows/              # n8n 워크플로우 JSON 파일
</pre>


---

## ⚙️ 주요 기능

- 📰 **FastAPI 뉴스 수집 및 vector db 구축 API**
- 🔗 **LangChain + Gemini 기반 뉴스 요약**
- 🔁 **n8n 워크플로우 기반 자동화**
- 📧 **사용자 맞춤 이메일 발송**
- 🔐 **Google Cloud 인증 연동**

---

## 🐳 실행 방법 (Docker Compose)

```bash
docker-compose up --build
