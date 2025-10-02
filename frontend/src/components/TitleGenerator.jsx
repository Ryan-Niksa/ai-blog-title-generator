import { useState } from "react";
import { fetchTitles } from "../api";
import React from "react";


export default function TitleGenerator({ onSelect }) {
  const [topic, setTopic] = useState("");
  const [titles, setTitles] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleGenerate = async (e) => {
    e.preventDefault();
    if (!topic.trim()) return;
    setLoading(true);
    try {
      const result = await fetchTitles(topic);
      setTitles(result);
    } catch (err) {
      alert("Error generating titles: " + err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">
      <h2>AI Blog Title Generator</h2>
      <form onSubmit={handleGenerate} className="form-row">
        <input
          type="text"
          placeholder="Enter a topic..."
          value={topic}
          onChange={(e) => setTopic(e.target.value)}
        />
        <button type="submit" disabled={loading}>
          {loading ? "Generating..." : "Generate Titles"}
        </button>
      </form>

      {titles.length > 0 && (
        <ul className="list">
          {titles.map((t, idx) => (
            <li key={idx}>
              {t}{" "}
              <button onClick={() => onSelect(t)} className="small-btn">
                Use
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
