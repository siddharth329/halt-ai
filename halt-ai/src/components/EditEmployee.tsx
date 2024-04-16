import React, { useState } from 'react'

const EditEmployeeId = ({machineId, setMachineIdInStorage}) => {
    const [employeeId, setEmployeeId] = useState(machineId)

    const onFormSubmit = e => {
        e.preventDefault()  
        setMachineIdInStorage(employeeId)
    }

    return (
        <div>
            <div className="plasmo-min-h-screen plasmo-flex plasmo-items-center plasmo-justify-center plasmo-w-full plasmo-dark:bg-gray-950">
                <div className="plasmo-bg-white plasmo-dark:bg-gray-900 plasmo-shadow-md plasmo-rounded-lg plasmo-px-8 plasmo-py-6 plasmo-max-w-md">
                    <h1 className="plasmo-text-2xl plasmo-font-bold plasmo-text-center plasmo-mb-4 plasmo-dark:text-gray-200">Register</h1>
                    <form onSubmit={e => onFormSubmit(e)}>
                        
                        <div className="plasmo-mb-4">
                            <label htmlFor="text" className="plasmo-block plasmo-text-sm plasmo-font-medium plasmo-text-gray-700 plasmo-dark:text-gray-300 plasmo-mb-2">Employee Id</label>
                            <input 
                                type="text" 
                                id="text" 
                                className="plasmo-shadow-sm plasmo-rounded-md plasmo-w-full plasmo-px-3 plasmo-py-2 plasmo-border plasmo-border-gray-300 plasmo-focus:outline-none plasmo-focus:ring-indigo-500 plasmo-focus:border-indigo-500" 
                                placeholder="John Doe" 
                                value={employeeId}
                                onChange={e => setEmployeeId(e.target.value)}
                                required={true} 
                            />
                        </div>
                        
                        <button type="submit" className="plasmo-w-full plasmo-flex plasmo-justify-center plasmo-py-2 plasmo-px-4 plasmo-border plasmo-border-transparent plasmo-rounded-md plasmo-shadow-sm plasmo-text-sm plasmo-font-medium plasmo-text-white plasmo-bg-indigo-600 plasmo-hover:bg-indigo-700 plasmo-focus:outline-none plasmo-focus:ring-2 plasmo-focus:ring-offset-2 plasmo-focus:ring-indigo-500">Update</button>
                    </form>
                </div>
            </div>
        </div>
    )
}

export default EditEmployeeId