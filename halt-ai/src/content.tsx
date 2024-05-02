import activateChatGPT from "~scripts/activateChatGPT"
import activateGemini from '~scripts/activateGemini'

export const config = {
  matches: ["https://chat.openai.com/*", 'https://gemini.google.com/*']
}

window.addEventListener("load", () => {
    if (window.location.origin.includes('chat.openai.com')) activateChatGPT()
    if (window.location.origin.includes('gemini.google.com')) activateGemini()
})

