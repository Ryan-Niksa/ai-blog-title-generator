import { deletePost } from "../api";
import React from "react";


export default function PostList({ posts, onDelete }) {
  if (!posts.length) {
    return <p className="empty">No blog posts yet.</p>;
  }

  const handleDelete = async (id) => {
    if (!window.confirm("Delete this post?")) return;
    await deletePost(id);
    onDelete(id);
  };

  return (
    <div className="card">
      <h2>All Blog Posts</h2>
      <ul className="list">
        {posts.map((p) => (
          <li key={p.id}>
            <h3>{p.title}</h3>
            <p>{p.content}</p>
            <small>Created: {new Date(p.created_at).toLocaleString()}</small>
            <div>
              <button onClick={() => handleDelete(p.id)} className="danger-btn">
                Delete
              </button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}
