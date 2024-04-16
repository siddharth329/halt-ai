export const getItemFromStorage = async ({ key }) => {
    let value = null
    const result = await chrome.storage.local.get(key)
    console.log(`Get Item Value: ${value}`)
    return result[key]
}

export const setItemInStorage = async ({ key, value }) => {
    chrome.storage.local.set({[key]: value})
    console.log(`Set Item Value: ${key} => ${value}`)
    return value
}