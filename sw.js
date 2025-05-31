const CACHE_NAME = "sakana-v1";
const BASE_URL = "https://discord-bot-py-theta.vercel.app";

const urlsToCache = [
  `${BASE_URL}/`,
  `${BASE_URL}/index.html`,
  `${BASE_URL}/favicon16x16.png`,
  `${BASE_URL}/favicon192x192.png`,
  `${BASE_URL}/favicon512x512.png`,
  `${BASE_URL}/style.css`,
  `${BASE_URL}/規制.py`,
  `${BASE_URL}/追記.py`,
  `${BASE_URL}/プレイ中.py`,
  `${BASE_URL}/chatbot.py`,
  "https://cdn.tailwindcss.com",
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"
];

self.addEventListener("install", event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener("fetch", event => {
  event.respondWith(
    caches.match(event.request).then(response => response || fetch(event.request))
  );
});

self.addEventListener("activate", event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(
        keys.map(key => {
          if (key !== CACHE_NAME) return caches.delete(key);
        })
      )
    )
  );
});