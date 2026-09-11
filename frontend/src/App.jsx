import { useState } from "react";

const API_URL = "http://localhost:8000";

export default function App() {
  const [resumeText, setResumeText] = useState("");
  const [jobDescription, setJobDescription] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  async function analyze(event) {
    event.preventDefault();
    setError("");
    setResult(null);

    try {
      const response = await fetch(`${API_URL}/match`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          resume_text: resumeText,
          job_description: jobDescription,
        }),
      });

      if (!response.ok) {
        throw new Error("Unable to analyze the documents.");
      }

      setResult(await response.json());
    } catch (requestError) {
      setError(requestError.message);
    }
  }

  return (
    <main style={{ maxWidth: 1000, margin: "40px auto", fontFamily: "Arial" }}>
      <h1>Resume & Job Match</h1>
      <p>Compare resume content against a job description.</p>

      <form onSubmit={analyze}>
        <label>
          Resume text
          <textarea
            rows="12"
            style={{ width: "100%", marginBottom: 20 }}
            value={resumeText}
            onChange={(event) => setResumeText(event.target.value)}
          />
        </label>

        <label>
          Job description
          <textarea
            rows="12"
            style={{ width: "100%", marginBottom: 20 }}
            value={jobDescription}
            onChange={(event) => setJobDescription(event.target.value)}
          />
        </label>

        <button type="submit">Analyze match</button>
      </form>

      {error && <p role="alert">{error}</p>}

      {result && (
        <section style={{ marginTop: 30 }}>
          <h2>Match score: {result.match_score}%</h2>
          <h3>Matched keywords</h3>
          <p>{result.matched_keywords.join(", ") || "None detected"}</p>

          <h3>Missing keywords</h3>
          <p>{result.missing_keywords.join(", ") || "None detected"}</p>

          <h3>Suggestions</h3>
          <ul>
            {result.suggestions.map((suggestion) => (
              <li key={suggestion}>{suggestion}</li>
            ))}
          </ul>
        </section>
      )}
    </main>
  );
}
