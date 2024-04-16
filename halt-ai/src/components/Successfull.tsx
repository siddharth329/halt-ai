import React from 'react'
import { Link } from 'react-router-dom'

const Successfull = ({machineId}) => {
  return (
    <div>
        {machineId == null ? (
            <Link to='/login'>Login</Link>
        ) : (
            
            <div className="plasmo-block plasmo-max-w-sm plasmo-p-6 plasmo-bg-white plasmo-border plasmo-border-gray-200 plasmo-rounded-lg plasmo-shadow plasmo-hover:bg-gray-100 plasmo-dark:bg-gray-800 plasmo-dark:border-gray-700 plasmo-dark:hover:bg-gray-700">
                <h5 className="plasmo-mb-2 plasmo-text-2xl plasmo-font-bold plasmo-tracking-tight plasmo-text-gray-900 plasmo-dark:text-white">Halt.AI</h5>
                <p className="plasmo-font-normal plasmo-text-gray-700 plasmo-dark:text-gray-400">Hi <strong>{machineId}</strong>, we are here to help your organization monitor your access to Generative AI platforms.</p>
                <br />
                <Link className='plasmo-text-blue-700' to='/edit'>Edit your Employee ID</Link>
            </div>

            // <div className='plasmo-flex plasmo-flex-col'>
            //     <h1 className=''>Successfull</h1>
            //     <div>{machineId}</div>
            //     <Link to='/login'>Edit</Link>
            // </div>
        )}
    </div>
  )
}

export default Successfull