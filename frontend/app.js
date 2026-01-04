const API_BASE = "/api";
const result = document.getElementById("result");

async function callAPI(path, body = null) {
  const res = await fetch(`${API_BASE}${path}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: body ? JSON.stringify(body) : null
  });

  if (!res.ok) {
    const text = await res.text();
    throw new Error(`${res.status} ${text}`);
  }

  return res.json();
}

// ▶ 생성
async function generate() {
  const specText = document.getElementById("spec").value.trim();
  if (!specText) {
    alert("요구사항을 입력하세요");
    return;
  }

  const data = await callAPI("/generate", {
    spec: specText
  });

  result.textContent = data.code;
}

// ▶ 수정
async function fix() {
  const code = result.textContent.trim();
  if (!code) {
    alert("수정할 코드가 없습니다");
    return;
  }

  const data = await callAPI("/fix", {
    payload: code
  });

  result.textContent = data.code;
}

// ▶ 테스트
async function testCode() {
  const data = await callAPI("/test", {});
  result.textContent =
    data.stdout || data.result || data.error || JSON.stringify(data, null, 2);
}

// ▶ 배포
async function deployCode() {
  const data = await callAPI("/deploy", {});
  result.textContent =
    data.result || data.message || JSON.stringify(data, null, 2);
}
