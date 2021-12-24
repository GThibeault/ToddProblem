import React from "react";
import Header from './components/Header';
import Footer from './components/Footer';
import "./index.css"
//import "./style.css";

export default function App() {
  const students = [
    ["Name", "Subject", "Marks"],
    ["ABC", "Arts", 80],
    ["XYZ", "Science", "70"],
  ];
  return (   
    <div>
       <Header title = {'Header component'}/>
      <table className="table">
        <thead>
          <tr className="thead">
            {students[0].map((item, index) => {
              return <th>{item}</th>;
            })}
          </tr>
        </thead>
        <tbody>
          {students.slice(1, students.length).map((item, index) => {
            return (
              <tr className="rows">
                <td>{item[0]}</td>
                <td>{item[1]}</td>
                <td>{item[2]}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
      <div class="flex-wrapper">
      <Footer/> 
      </div>
      
    </div>
  );
}