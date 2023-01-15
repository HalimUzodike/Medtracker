import React, { Component } from 'react';

class MedicationTracker extends Component {
    constructor(props) {
        super(props);
        this.state = {
            medications: [],
            medicationName: '',
            dosage: '',
            frequency: '',
        };
    }

    handleSubmit = (e) => {
        e.preventDefault();
        const newMedication = {
            name: this.state.medicationName,
            dosage: this.state.dosage,
            frequency: this.state.frequency
        };
        this.setState(prevState => ({
            medications: [...prevState.medications, newMedication],
            medicationName: '',
            dosage: '',
            frequency: '',
        }));
    }

    handleDelete = (index) => {
        this.setState(prevState => ({
            medications: prevState.medications.filter((medication, i) => i !== index)
        }));
    }

    handleEdit = (index) => {
        const selectedMedication = this.state.medications[index];
        this.setState({
            medicationName: selectedMedication.name,
            dosage: selectedMedication.dosage,
            frequency: selectedMedication.frequency,
            isEditing: true,
            selectedIndex: index
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