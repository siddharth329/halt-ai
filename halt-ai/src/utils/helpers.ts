// @ts-nocheck

export const showLoading = () => {
	var newElement = document.createElement("div")
	newElement.setAttribute("id", "loadingForChecking")
	newElement.style.position = "absolute"
	newElement.style.left = "50%"
	newElement.style.top = "50%"
	newElement.style.transform = "translate(-50%, -50%)"
	newElement.style.padding = "40px"
	newElement.style.backgroundColor = "rgba(0,150,0,0.95)"
	newElement.style.color = "white"
	newElement.style.borderRadius = "10px"
	newElement.style.zIndex = '1000'
	newElement.style.fontFamily = 'sans-serif'
	newElement.textContent = "Checking Query ..."
	document.body.appendChild(newElement)
	return () => {
		console.log('Remove Script ran')
		newElement.remove()
	}
}

export const showError = (error) => {
	var newElement = document.createElement("div")
	newElement.setAttribute("id", "errorInChecking")
	newElement.style.position = "absolute"
	newElement.style.left = "50%"
	newElement.style.top = "50%"
	newElement.style.transform = "translate(-50%, -50%)"
	newElement.style.padding = "40px"
	newElement.style.backgroundColor = "rgb(255,255,255)"
	newElement.style.color = "red"
	newElement.style.border = "1px solid red"
	newElement.style.borderRadius = "10px"
	newElement.style.display = "flex"
	newElement.style.flexDirection = "column"
	newElement.innerHTML = `<span><strong>ALERT!</strong> ${error}</span>`
	newElement.style.zIndex = '1000'
	newElement.style.fontFamily = 'sans-serif'
	document.body.appendChild(newElement)
	return () => newElement.remove()
}