import React, { useState } from 'react'

export default function FarePredictor() {
    const [pickup, setPickup] = useState("");
    const [dropoff, setDropoff] = useState("");
    const [fare, setFare] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
}