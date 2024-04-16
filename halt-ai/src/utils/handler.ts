// @ts-nocheck
import { useStorage } from "@plasmohq/storage/hook";
import axios from "axios";

import { getItemFromStorage } from "./storage";

class APIHandler {
    constructor() {
        this.BASE_URL = 'https://7d89-110-227-54-189.ngrok-free.app'
    }

    async checkQuery({ content, source }) {

        try {
            const URL = `${this.BASE_URL}/api/query/`
            const machine_id = await getItemFromStorage({key: 'machineId'})
            console.log(machine_id)
            // const machineIdFromStorage = getItemFromStorage({key: 'machineId'});
            const payload = { source, content, machine_id }
            const { data } = await axios.post(URL, payload)
            return data

        } catch {
            alert('Error reaching server!')
            return { blocked: true }
        }
    }
}

export default APIHandler