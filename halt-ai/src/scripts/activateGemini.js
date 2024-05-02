// @ts-nocheck
import APIHandler from "../utils/handler"
import { showError, showLoading } from "../utils/helpers"

const geminiCleanup = () => {
	const buttonElement = document.querySelector(
		'button[aria-label="Send message"]'
	)
	const imageElement = document.querySelector(
		'button[mattooltip="Upload Image"]'
	)
	if (buttonElement) buttonElement.style.display = "none"
	if (imageElement) imageElement.style.display = "none"

	return buttonElement
}

const activateGemini = () => {
	let buttonElement = geminiCleanup()
	document.addEventListener("change", () => (buttonElement = geminiCleanup()))

	const textarea = document.querySelector(
		'div[data-placeholder="Enter a prompt here"]'
	)
	// const textarea = document.querySelector("#prompt-textarea")

	if (textarea) {
		textarea.addEventListener("keydown", async (event) => {
			event.stopPropagation()

			if (event.keyCode === 13 && !event.shiftKey) {
				event.preventDefault()

				const removeLoading = showLoading()
				const handler = new APIHandler()
				const data = await handler.checkQuery({
					content: textarea.textContent,
					source: 1
				})
				removeLoading()

				if (data.source === 1 && data.blocked === false) {
					buttonElement.click()
				} else if (data.blocked === true) {
					const removeError = showError(data.error)
					setTimeout(() => removeError(), 10000)
				}

				buttonElement = geminiCleanup()
			}
		})
	}
}

export default activateGemini
