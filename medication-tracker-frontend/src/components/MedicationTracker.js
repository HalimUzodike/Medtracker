import React, { Component } from 'react';
import './MedicationTracker.css';
import axios from 'axios';

class MedicationTracker extends Component {
    constructor(props) {
        super(props);
        this.state = {
            medications: [],
            medicationName: '',
            dosage: '',
            frequency: '',
            notes: '',
        };
    }

    componentDidMount() {
        // Get initial data from the backend
        axios.get('http://localhost:5000/medications')
            .then(res => this.setState({ medications: res.data }))
            .catch(err => console.log(err));
    }

    handleSubmit = (e) => {
        e.preventDefault();
        const newMedication = {
            name: this.state.medicationName,
            dosage: this.state.dosage,
            frequency: this.state.frequency,
            notes: this.state.notes
        };

        // Send the new medication data to the backend
        axios.post('http://localhost:5000/medications', newMedication)
            .then(res => {
                this.setState(prevState => ({
                    medications: [...prevState.medications, res.data],
                    medicationName: '',
                    dosage: '',
                    frequency: '',
                    notes: ''
                }));
            })
            .catch(err => console.log(err));
    }


    handleDelete = (index) => {
        // Delete the medication from the backend
        axios.delete(`http://localhost:5000/medications/${index}`)
            .then(res => {
                this.setState(prevState => ({
                    medications: prevState.medications.filter((medication, i) => i !== index)
                }));
            })
            .catch(err => console.log(err));
    }

    handleEdit = (index) => {
        const selectedMedication = this.state.medications[index];
        this.setState({
            medicationName: selectedMedication.name,
            dosage: selectedMedication.dosage,
            frequency: selectedMedication.frequency,
            notes: selectedMedication.notes,
            isEditing: true,
            selectedIndex: index
        });
    
        axios.put(`/api/medications/${selectedMedication._id}`, {
            name: this.state.medicationName,
            dosage: this.state.dosage,
            frequency: this.state.frequency,
            notes: this.state.notes
        })
        .then(response => {
            console.log(response);
            this.setState(prevState => ({
                medications: prevState.medications.map((medication, i) => {
                    if (i !== this.state.selectedIndex) {
                        return medication;
                    } else {
                        return {...medication, ...response.data};
                    }
                }),
                isEditing: false,
                medicationName: '',
                dosage: '',
                frequency: '',
                notes: '',
                selectedIndex: null
            }));
        })
        .catch(error => {
            console.log(error);
        });
    }
    

    render() {
        return (
            <div>
                <form onSubmit={this.handleSubmit}>
                    <label>
                        Medication Name:
                        <input type="text" value={this.state.medicationName} onChange={(e) => this.setState({ medicationName: e.target.value })} />
                    </label>
                    <br />
                    <label>
                        Dosage:
                        <input type="text" value={this.state.dosage} onChange={(e) => this.setState({ dosage: e.target.value })} />
                    </label>
                    <br />
                    <label>
                        Frequency:
                        <input type="text" value={this.state.frequency} onChange={(e) => this.setState({ frequency: e.target.value })} />
                    </label>
                    <br />
                    <label>
                        Notes:
                        <textarea value={this.state.notes} onChange={(e) => this.setState({ notes: e.target.value })} />
                    </label>
                    <br />
                    <button type="submit">Add Medication</button>
                </form>
                <div>
                    <h2>Medications</h2>
                    <table>
                        <thead>
                            <tr>
                                <th>Name</th>
                                <th>Dosage</th>
                                <th>Frequency</th>
                                <th>Notes</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                            {
                                this.state.medications.map((medication, index) => (
                                    <tr key={index}>
                                        <td>{medication.name}</td>
                                        <td>{medication.dosage}</td>
                                        <td>{medication.frequency}</td>
                                        <td>{medication.notes}</td>
                                        <td>
                                            <button onClick={() => this.handleDelete(index)}>Delete</button>
                                            <button onClick={() => this.handleEdit(index)}>Edit</button>
                                        </td>
                                    </tr>
                                ))
                            }
                        </tbody>
                    </table>
                </div>
            </div>
        );
    }
}

export default MedicationTracker;