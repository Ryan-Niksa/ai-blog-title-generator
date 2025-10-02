import React, { useEffect, useState } from "react";
import "./App.css";
import TitleGenerator from "./components/TitleGenerator.jsx";
import PostForm from "./components/PostForm.jsx";
import PostList from "./components/PostList.jsx";
import { fetchPosts } from "./api.js";

export default function App() {
  const [posts, setPosts] = useState([]);
  const [selectedTitle, setSelectedTitle] = useState("");

  useEffect(() => {
    const loadPosts = async () => {
      try {
        const data = await fetchPosts();
        setPosts(data);
      } catch (err) {
        console.error("Error loading posts:", err);
      }
    };
    loadPosts();
  }, []);

  const handleNewPost = (post) => {
    setPosts((prev) => [post, ...prev]);
  };

  const handleDelete = (id) => {
    setPosts((prev) => prev.filter((p) => p.id !== id));
  };

  return (
    <div className="container">
      <h1>AI Blog Title Generator + Mini CMS</h1>

      <TitleGenerator onSelect={(title) => setSelectedTitle(title)} />

      <PostForm onNewPost={handleNewPost} initialTitle={selectedTitle} />

      <PostList posts={posts} onDelete={handleDelete} />
    </div>
  );
}
