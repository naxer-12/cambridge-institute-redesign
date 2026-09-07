import http from "node:http";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const PORT = process.env.PORT || 3000;
const DATA_DIR = path.join(__dirname, "data");
const CSV_FILE = path.join(DATA_DIR, "inquiries.csv");
const STATIC_DIR = fs.existsSync(path.join(__dirname, "dist")) 
  ? path.join(__dirname, "dist") 
  : __dirname;

const MIME_TYPES = {
  ".html": "text/html",
  ".css": "text/css",
  ".js": "application/javascript",
  ".json": "application/json",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".svg": "image/svg+xml",
  ".ico": "image/x-icon",
  ".csv": "text/csv"
};

function escapeCsv(val) {
  return `"${String(val ?? "").replace(/"/g, """")}"`;
}

function saveInquiry(data) {
  if (!fs.existsSync(DATA_DIR)) {
    fs.mkdirSync(DATA_DIR, { recursive: true });
  }

  const fileExists = fs.existsSync(CSV_FILE);
  const headers = ["Timestamp", "Full Name", "Phone", "Email", "Coaching", "Message", "Source Page"];

  const now = new Date();
  const pad = (n) => String(n).padStart(2, "0");
  const timestamp = `${now.getFullYear()}-${pad(now.getMonth() + 1)}-${pad(now.getDate())} ${pad(now.getHours())}:${pad(now.getMinutes())}:${pad(now.getSeconds())}`;

  const row = [
    escapeCsv(timestamp),
    escapeCsv(data.name || ""),
    escapeCsv(data.phone || ""),
    escapeCsv(data.email || ""),
    escapeCsv(data.coaching || ""),
    escapeCsv(data.message || ""),
    escapeCsv(data.page || "")
  ].join(",") + "\n";

  if (!fileExists) {
    fs.writeFileSync(CSV_FILE, headers.map(escapeCsv).join(",") + "\n" + row, "utf8");
  } else {
    fs.appendFileSync(CSV_FILE, row, "utf8");
  }
}

const server = http.createServer((req, res) => {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "GET, POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");

  if (req.method === "OPTIONS") {
    res.writeHead(204);
    res.end();
    return;
  }

  if (req.url === "/api/inquiry" && req.method === "POST") {
    let body = "";
    req.on("data", (chunk) => {
      body += chunk;
    });
    req.on("end", () => {
      try {
        const data = JSON.parse(body || "{}");
        saveInquiry(data);
        res.writeHead(200, { "Content-Type": "application/json" });
        res.end(JSON.stringify({ 
          success: true, 
          message: "Inquiry successfully saved to CSV",
          file: "data/inquiries.csv"
        }));
      } catch (err) {
        res.writeHead(500, { "Content-Type": "application/json" });
        res.end(JSON.stringify({ success: false, message: err.message || "Internal Server Error" }));
      }
    });
    return;
  }

  let filePath = path.join(STATIC_DIR, req.url === "/" ? "index.html" : req.url.split("?")[0]);
  if (!path.extname(filePath)) {
    filePath += ".html";
  }

  fs.stat(filePath, (err, stats) => {
    if (err || !stats.isFile()) {
      res.writeHead(404, { "Content-Type": "text/plain" });
      res.end("404 Not Found");
      return;
    }

    const ext = path.extname(filePath).toLowerCase();
    const contentType = MIME_TYPES[ext] || "application/octet-stream";
    res.writeHead(200, { "Content-Type": contentType });
    fs.createReadStream(filePath).pipe(res);
  });
});

server.listen(PORT, () => {
  console.log(`Cambridge Institute Server running at http://localhost:${PORT}`);
  console.log(`Saving form submissions to: ${CSV_FILE}`);
});
