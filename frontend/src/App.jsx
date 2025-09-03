import React from 'react'

const App = () => {
  return (
    <div>
      <div className="min-h-screen bg-gradient-to-br from-yellow-100 to-yellow-200 flex flex-col">
      {/* Navbar */}
      <header className="bg-yellow-400 shadow-md p-4 flex justify-between items-center">
        <h1 className="text-2xl font-extrabold text-black tracking-wide">
          NYC Taxi Fare Predictor
        </h1>
        <nav>
          <button className="text-black hover:text-gray-800 font-medium">
            About
          </button>
        </nav>
      </header>

      {/* Main content */}
      <main className="flex flex-1 items-center justify-center p-6">
        <div className="w-full max-w-lg bg-white rounded-2xl shadow-xl p-8 border-2 border-yellow-400">
          <h2 className="text-xl font-semibold text-gray-900 mb-6 text-center">
            Enter Your Trip Details
          </h2>

          {/* Input form */}
          <form className="space-y-4">
            <div>
              <label className="block text-gray-800 font-medium mb-1">
                Pickup Location
              </label>
              <input
                type="text"
                placeholder="e.g. Empire State Building"
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-yellow-400 focus:outline-none"
              />
            </div>

            <div>
              <label className="block text-gray-800 font-medium mb-1">
                Dropoff Location
              </label>
              <input
                type="text"
                placeholder="e.g. Times Square"
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-yellow-400 focus:outline-none"
              />
            </div>

            <button
              type="submit"
              className="w-full bg-yellow-400 hover:bg-yellow-500 text-black font-bold py-3 rounded-lg shadow-md transition"
            >
              Predict Fare 
            </button>
          </form>

          {/* Result placeholder */}
          <div className="mt-6 text-center text-gray-700 font-medium">
            Your predicted fare will appear here.
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="text-center text-black font-semibold text-sm p-4 bg-yellow-400">
        © 2025 NYC Taxi Fare Predictor
      </footer>
    </div>
    </div>
  )
}

export default App
