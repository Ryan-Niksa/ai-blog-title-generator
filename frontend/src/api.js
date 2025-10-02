import axios from "axios";

const API_BASE = "http://127.0.0.1:8000/api";

export async function fetchTitles(topic, n = 5) {
  const res = await axios.get(`${API_BASE}/titles`, { params: { topic, n } });
  return res.data;
}

export async function createPost(post) {
  const res = await axios.post(`${API_BASE}/posts`, post);
  return res.data;
}

export async function fetchPosts() {
  const res = await axios.get(`${API_BASE}/posts`);
  return res.data;
}

export async function updatePost(id, post) {
  const res = await axios.put(`${API_BASE}/posts/${id}`, post);
  return res.data;
}

export async function deletePost(id) {
  const res = await axios.delete(`${API_BASE}/posts/${id}`);
  return res.data;
}
