async function callAPI(path, body = {}) {
  const res = await fetch(`${API_BASE}${path}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body)
  });
  return res.json();
}

async function generate() {
  const spec = document.getElementById("spec").value;
  const data = await callAPI("/generate", { spec });
  result.textContent = data.code;
}

async function fix() {
  const payload = { code: result.textContent };
  const data = await callAPI("/fix", payload);
  result.textContent = data.code;
}

async function testCode() {
  const data = await callAPI("/test");
  result.textContent = data.stdout || data.stderr;
}

async function deployCode() {
  const data = await callAPI("/deploy");
  result.textContent = data.result;
}
