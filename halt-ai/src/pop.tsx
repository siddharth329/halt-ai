import { useEffect, useState } from "react"
import { MemoryRouter, Routes, Route, useNavigate } from "react-router-dom"

import EmployeeId from "~components/EmployeeId"
import EditEmployeeId from "~components/EditEmployee"
import Successfull from "~components/Successfull"
import { getItemFromStorage, setItemInStorage } from "~utils/storage"

import "~style.css"

function Main() {
	const [machineId, setMachineId] = useState(null)
	const navigate = useNavigate();

	useEffect(() => {
		useEffectFunction()
	}, [])

	const useEffectFunction = async () => {
		const machineIdFromStorage = await getItemFromStorage({key: 'machineId'});
		setMachineId(machineIdFromStorage)
	}

	const setMachineIdInStorage = async machineId => {
		await setItemInStorage({key: 'machineId', value: machineId})
		setMachineId(machineId)
		navigate('/')
	}

	console.log(machineId === undefined)
	return (
		<div className="plasmo-flex plasmo-items-center plasmo-justify-center">
		<div className="plasmo-w-[400px] plasmo-h-[500px] plasmo-flex plasmo-justify-center plasmo-items-center">
			{/* <MemoryRouter> */}
				<Routes>
					<Route path="/login" element={<EmployeeId setMachineIdInStorage={setMachineIdInStorage} />} />
					<Route path="/edit" element={<EditEmployeeId machineId={machineId} setMachineIdInStorage={setMachineIdInStorage} />} />
					<Route path="/" element={<Successfull machineId={machineId} />} />
				</Routes>
			{/* </MemoryRouter> */}
		</div>
		</div>
	)
}

function IndexPopup() {
	return (
		<MemoryRouter>
			<Main />
		</MemoryRouter>
	)
}

export default IndexPopup
