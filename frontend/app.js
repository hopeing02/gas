const API_BASE = "/api";

const result = document.getElementById("result");

async function callAPI(path, body = {}) {
  const res = await fetch(`${API_BASE}${path}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body)
  });

  if (!res.ok) {
    const text = await res.text();
    throw new Error(`${res.status} ${text}`);
  }

  return res.json();
}

async function generate() {
  const specText = document.getElementById("spec").value;

  const data = await callAPI("/generate", {
    spec: {
      description: specText
    }
  });

  result.textContent = data.code;
}

async function fix() {
  const code = result.textContent;

  const data = await callAPI("/fix", {
    code
  });

  result.textContent = data.code;
}

async function testCode() {
  const data = await callAPI("/test");
  result.textContent = data.stdout || data.stderr || JSON.stringify(data);
}

async function deployCode() {
  const data = await callAPI("/deploy");
  result.textContent = data.result || JSON.stringify(data);
}
