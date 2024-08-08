import React, { useState } from "react";
import "../App.css";

const AddDataForm = ({ onAddData }) => {
  const [dataType, setDataType] = useState("PDF");
  const [dataLink, setDataLink] = useState("");
  const [dataFile, setDataFile] = useState(null);
  const [dataName, setDataName] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    const newData = {
      name: dataName,
      type: dataType,
      link: dataType === "Link" ? dataLink : "",
      file: dataType === "PDF" ? dataFile : null,
      status: "Pending",
      date: new Date().toLocaleString(),
    };
    onAddData(newData);
    setDataName("");
    setDataLink("");
    setDataFile(null);
    setDataType("PDF");
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Data Name:</label>
        <input
          type="text"
          value={dataName}
          onChange={(e) => setDataName(e.target.value)}
        />
      </div>
      <div>
        <label>Data Type:</label>
        <select value={dataType} onChange={(e) => setDataType(e.target.value)}>
          <option value="PDF">PDF</option>
          <option value="Link">Link</option>
        </select>
      </div>
      {dataType === "Link" && (
        <div>
          <label>Link URL:</label>
          <input
            type="text"
            value={dataLink}
            onChange={(e) => setDataLink(e.target.value)}
          />
        </div>
      )}
      {dataType === "PDF" && (
        <div>
          <label>Upload PDF:</label>
          <input
            type="file"
            accept="application/pdf"
            onChange={(e) => setDataFile(e.target.files[0])}
          />
        </div>
      )}
      <button type="submit">Add Data</button>
    </form>
  );
};

export default AddDataForm;
