function getState(promise) {
  const t = {}
  return Promise.race([promise, t]).then((p) => p === t ? "pending" : "fulfilled", () => "rejected")
}