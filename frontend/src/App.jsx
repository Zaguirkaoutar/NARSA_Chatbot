import ChatBox from "./components/ChatBox.jsx";
import FaqSection from "./components/FaqSection.jsx";
import FeedbackBox from "./components/FeedbackBox.jsx";

export default function App() {
  return (
    <main className="app-container">
      <header>
        <h1>NARSA AI Assistant</h1>
        <p>Interface conversationnelle d'assistance aux usagers NARSA.</p>
      </header>
      <ChatBox />
      <FaqSection />
      <FeedbackBox />
    </main>
  );
}
