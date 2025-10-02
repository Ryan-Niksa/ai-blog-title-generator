import { useState, useEffect } from "react";
import { createPost } from "../api";
import React from "react";

export default function PostForm({ onNewPost, initialTitle }) {
  const [title, setTitle] = useState(initialTitle || "");
  const [content, setContent] = useState("");
  const [loading, setLoading] = useState(false);

  // auto-update title if user clicks "Use" from TitleGenerator
  useEffect(() => {
    if (initialTitle) setTitle(initialTitle);
  }, [initialTitle]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!title.trim() || !content.trim()) return;
    setLoading(true);
    try {
      const newPost = await createPost({ title, content });
      onNewPost(newPost);
      setTitle("");
      setContent("");
    } catch (err) {
      alert("Error creating post: " + err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">
      <h2>Create Blog Post</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Post title..."
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <textarea
          rows={6}
          placeholder="Write blog content..."
          value={content}
          onChange={(e) => setContent(e.target.value)}
        />
        <button type="submit" disabled={loading}>
          {loading ? "Saving..." : "Save Post"}
        </button>
      </form>
    </div>
  );
}
