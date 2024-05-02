// @ts-nocheck
import APIHandler from "../utils/handler"
import { showError, showLoading } from "../utils/helpers"

const cleanup = () => {
	const buttonElement = document.querySelector(
		'button[data-testid="send-button"]'
	)
	if (buttonElement) {
		buttonElement.style.display = "none"
	}
	return buttonElement
}

const changeTextAreaContents = async (element, content) => {
	element.click()
	element.textContent = content
	element.dispatchEvent(new Event("input", { bubbles: true }))
}

const activateChatGPT = () => {
	let buttonElement = cleanup()
	document.addEventListener("change", () => (buttonElement = cleanup()))

	const textarea = document.querySelector('textarea[id="prompt-textarea"]')

	if (textarea) {
		textarea.addEventListener("keydown", async (event) => {
			event.stopPropagation()

			if (event.keyCode === 13 && !event.shiftKey) {
				event.preventDefault()

				const removeLoading = showLoading()
				const handler = new APIHandler()
				const data = await handler.checkQuery({
					content: textarea.textContent,
					source: 0
				})
				removeLoading()

				if (data.source === 0 && data.blocked === false) {
					const textarea1 = document.querySelector(
						"textarea[tabindex='0']"
					)
					textarea1.value = data.content
					textarea1.dispatchEvent(
						new Event("input", { bubbles: true })
					)
					buttonElement.click()
				} else if (data.blocked === true) {
					const removeError = showError(data.error)
					setTimeout(() => removeError(), 10000)
				}

				buttonElement = cleanup()
			}
		})
	}
}

export default activateChatGPT
