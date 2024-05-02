// @ts-nocheck
import axios from "axios";

import { getItemFromStorage } from "./storage";

class APIHandler {
    constructor() {
        this.BASE_URL = 'https://wahoo-wanted-truly.ngrok-free.app'
    }

    async checkQuery({ content, source }) {
        try {
            const URL = `${this.BASE_URL}/api/query/`
            const machine_id = await getItemFromStorage({key: 'machineId'})
            if (machine_id === undefined) {
                return {
                    "blocked": true,
                    "error": " Please Log In to Halt.AI",
                }
            } else {
                const payload = { source, content, machine_id }
                const { data } = await axios.post(URL, payload)
                return data
            } 
        } catch {
            alert('Error reaching server!')
            return { blocked: true }
        }
    }
}

export default APIHandler