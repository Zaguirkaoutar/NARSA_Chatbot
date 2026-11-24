export default function ChatBox() {
  return (
    <section aria-label="Interface conversationnelle">
      <h2>Discussion</h2>
      <p>Emplacement prévu pour l'affichage des messages et la saisie.</p>
      <form onSubmit={(e) => e.preventDefault()}>
        <input
          type="text"
          placeholder="Posez votre question sur les services NARSA..."
          aria-label="Message"
        />
        <button type="submit">Envoyer</button>
      </form>
    </section>
  );
}

