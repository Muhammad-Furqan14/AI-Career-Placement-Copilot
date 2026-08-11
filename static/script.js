// ==========================================
// AI CAREER PLACEMENT COPILOT
// JAVASCRIPT
// ==========================================


// ==========================================
// DOM ELEMENTS
// ==========================================

const cvInput = document.getElementById("cv");
const uploadBox = document.getElementById("uploadBox");
const uploadIcon = document.getElementById("uploadIcon");
const uploadTitle = document.getElementById("uploadTitle");
const uploadText = document.getElementById("uploadText");
const selectedFile = document.getElementById("selectedFile");
const fileName = document.getElementById("fileName");
const fileSize = document.getElementById("fileSize");
const removeFile = document.getElementById("removeFile");

const previewEmpty = document.getElementById("previewEmpty");
const pdfPreview = document.getElementById("pdfPreview");
const pdfViewer = document.getElementById("pdfViewer");
const previewInfo = document.getElementById("previewInfo");
const previewStatus = document.getElementById("previewStatus");

const jobDescription = document.getElementById("jobDescription");
const characterCount = document.getElementById("characterCount");

const analyzeButton = document.getElementById("analyzeButton");
const loading = document.getElementById("loading");
const results = document.getElementById("results");

const themeToggle = document.getElementById("themeToggle");
const themeIcon = document.getElementById("themeIcon");
const themeText = document.getElementById("themeText");

let pdfURL = null;


// ==========================================
// FORMAT FILE SIZE
// ==========================================

function formatFileSize(bytes) {

    if (bytes < 1024) {
        return bytes + " Bytes";
    }

    if (bytes < 1024 * 1024) {
        return (bytes / 1024).toFixed(1) + " KB";
    }

    return (bytes / (1024 * 1024)).toFixed(2) + " MB";
}


// ==========================================
// HANDLE CV FILE
// ==========================================

function handleFile() {

    const file = cvInput.files[0];

    if (!file) {
        return;
    }


    // Check PDF type

    if (
        file.type !== "application/pdf" &&
        !file.name.toLowerCase().endsWith(".pdf")
    ) {

        alert("Please upload a PDF file only.");

        cvInput.value = "";

        return;
    }


    // Remove previous PDF preview URL

    if (pdfURL) {
        URL.revokeObjectURL(pdfURL);
    }


    // Create new preview

    pdfURL = URL.createObjectURL(file);

    pdfViewer.src = pdfURL;


    // Display file information

    fileName.textContent = file.name;

    fileSize.textContent =
        formatFileSize(file.size);


    selectedFile.classList.remove("hidden");


    // Update upload section

    uploadBox.classList.add("file-selected");

    uploadIcon.textContent = "📄";

    uploadTitle.textContent =
        "CV Selected Successfully";

    uploadText.textContent =
        "Your resume is ready for AI analysis";


    // Update PDF preview

    previewEmpty.classList.add("hidden");

    pdfPreview.classList.remove("hidden");

    previewInfo.classList.remove("hidden");

    previewStatus.textContent = "Ready";

    previewStatus.classList.add("ready");
}


// ==========================================
// FILE INPUT CHANGE
// ==========================================

cvInput.addEventListener(
    "change",
    handleFile
);


// ==========================================
// REMOVE CV
// ==========================================

removeFile.addEventListener(
    "click",
    function (event) {

        event.preventDefault();
        event.stopPropagation();


        // Clear file input

        cvInput.value = "";


        // Remove preview URL

        if (pdfURL) {

            URL.revokeObjectURL(pdfURL);

            pdfURL = null;
        }


        pdfViewer.src = "";


        // Reset upload section

        selectedFile.classList.add("hidden");

        uploadBox.classList.remove("file-selected");

        uploadIcon.textContent = "☁️";

        uploadTitle.textContent = "Upload your CV";

        uploadText.textContent =
            "Drag and drop or click to browse";


        // Reset PDF preview

        pdfPreview.classList.add("hidden");

        previewInfo.classList.add("hidden");

        previewEmpty.classList.remove("hidden");

        previewStatus.textContent = "Waiting";

        previewStatus.classList.remove("ready");


        // Hide old results

        results.classList.add("hidden");
    }
);


// ==========================================
// DRAG AND DROP
// ==========================================

uploadBox.addEventListener(
    "dragover",
    function (event) {

        event.preventDefault();

        uploadBox.classList.add("drag-active");
    }
);


uploadBox.addEventListener(
    "dragleave",
    function () {

        uploadBox.classList.remove("drag-active");
    }
);


uploadBox.addEventListener(
    "drop",
    function (event) {

        event.preventDefault();

        uploadBox.classList.remove("drag-active");


        const files = event.dataTransfer.files;


        if (files.length > 0) {

            // Check PDF before assigning

            const droppedFile = files[0];

            if (
                droppedFile.type !== "application/pdf" &&
                !droppedFile.name
                    .toLowerCase()
                    .endsWith(".pdf")
            ) {

                alert("Please upload a PDF file only.");

                return;
            }


            // Assign dropped file

            const dataTransfer =
                new DataTransfer();

            dataTransfer.items.add(
                droppedFile
            );

            cvInput.files =
                dataTransfer.files;


            handleFile();
        }
    }
);


// ==========================================
// CHARACTER COUNTER
// ==========================================

jobDescription.addEventListener(
    "input",
    function () {

        characterCount.textContent =
            jobDescription.value.length +
            " characters";
    }
);


// ==========================================
// THEME TOGGLE
// ==========================================

themeToggle.addEventListener(
    "click",
    function () {

        document.body.classList.toggle(
            "dark"
        );


        const isDark =
            document.body.classList.contains(
                "dark"
            );


        if (isDark) {

            themeIcon.textContent = "☀️";

            themeText.textContent = "Light";

            localStorage.setItem(
                "theme",
                "dark"
            );

        } else {

            themeIcon.textContent = "🌙";

            themeText.textContent = "Dark";

            localStorage.setItem(
                "theme",
                "light"
            );
        }
    }
);


// ==========================================
// LOAD SAVED THEME
// ==========================================

window.addEventListener(
    "DOMContentLoaded",
    function () {

        const savedTheme =
            localStorage.getItem("theme");


        if (savedTheme === "dark") {

            document.body.classList.add(
                "dark"
            );

            themeIcon.textContent = "☀️";

            themeText.textContent = "Light";

        } else {

            themeIcon.textContent = "🌙";

            themeText.textContent = "Dark";
        }
    }
);


// ==========================================
// ANALYZE CAREER
// ==========================================

analyzeButton.addEventListener(
    "click",
    async function () {

        const file = cvInput.files[0];

        const jobText =
            jobDescription.value.trim();


        // Validate CV

        if (!file) {

            alert(
                "Please upload your CV first."
            );

            return;
        }


        // Validate job description

        if (!jobText) {

            alert(
                "Please enter the job description."
            );

            return;
        }


        // Show loading

        loading.classList.remove("hidden");

        results.classList.add("hidden");

        analyzeButton.disabled = true;

        analyzeButton.style.opacity = "0.7";


        try {

            // Create form data

            const formData = new FormData();

            formData.append(
                "cv",
                file
            );

            formData.append(
                "job_description",
                jobText
            );


            // Send request to FastAPI

            const response =
                await fetch(
                    "/analyze",
                    {
                        method: "POST",
                        body: formData
                    }
                );


            // Read backend response

            const data =
                await response.json();


            // Check HTTP error

            if (!response.ok) {

                throw new Error(
                    data.error ||
                    "Server error during analysis."
                );
            }


            // IMPORTANT:
            // Check backend success value.
            // This prevents fake 0% results.

            if (!data.success) {

                throw new Error(
                    data.error ||
                    "CV analysis failed."
                );
            }


            // Display successful results

            displayResults(data);

        }


        catch (error) {

            console.error(
                "Analysis Error:",
                error
            );


            alert(
                error.message ||
                "Error analyzing your career profile."
            );

        }


        finally {

            // Hide loading

            loading.classList.add("hidden");

            analyzeButton.disabled = false;

            analyzeButton.style.opacity = "1";
        }

    }
);


// ==========================================
// DISPLAY RESULTS
// ==========================================

function displayResults(data) {


    // ======================================
    // GET DATA SAFELY
    // ======================================

    const score =
        Number(data.match_score) || 0;


    const matched =
        Array.isArray(data.matched_skills)
            ? data.matched_skills
            : [];


    const missing =
        Array.isArray(data.missing_skills)
            ? data.missing_skills
            : [];


    const roadmapData =
        Array.isArray(data.roadmap)
            ? data.roadmap
            : [];


    // ======================================
    // MATCH SCORE
    // ======================================

    const matchScore =
        document.getElementById(
            "matchScore"
        );


    if (matchScore) {

        matchScore.textContent =
            score + "%";
    }


    // ======================================
    // MATCHED SKILLS
    // ======================================

    const matchedSkills =
        document.getElementById(
            "matchedSkills"
        );


    if (matchedSkills) {

        matchedSkills.innerHTML = "";


        if (matched.length === 0) {

            matchedSkills.innerHTML =
                "<p>No matched skills found.</p>";

        } else {

            matched.forEach(
                function (skill) {

                    const tag =
                        document.createElement(
                            "span"
                        );


                    tag.className =
                        "skill-tag matched";


                    tag.textContent =
                        skill;


                    matchedSkills.appendChild(
                        tag
                    );
                }
            );
        }
    }


    // ======================================
    // MISSING SKILLS
    // ======================================

    const missingSkills =
        document.getElementById(
            "missingSkills"
        );


    if (missingSkills) {

        missingSkills.innerHTML = "";


        if (missing.length === 0) {

            missingSkills.innerHTML =
                "<p>No major skill gaps found.</p>";

        } else {

            missing.forEach(
                function (skill) {

                    const tag =
                        document.createElement(
                            "span"
                        );


                    tag.className =
                        "skill-tag missing";


                    tag.textContent =
                        skill;


                    missingSkills.appendChild(
                        tag
                    );
                }
            );
        }
    }


    // ======================================
    // PERSONALIZED LEARNING ROADMAP
    // ======================================

    const roadmap =
        document.getElementById(
            "roadmap"
        );


    if (roadmap) {

        roadmap.innerHTML = "";


        if (roadmapData.length > 0) {

            roadmapData.forEach(
                function (item, index) {

                    const step =
                        document.createElement(
                            "div"
                        );


                    step.className =
                        "roadmap-step";


                    // Get values from backend object

                    const stepNumber =
                        item.step ??
                        (index + 1);


                    const skill =
                        item.skill ??
                        "Skill";


                    const recommendation =
                        item.recommendation ??
                        "Learn the fundamentals of this skill.";


                    // Display roadmap correctly
                    // NOT [object Object]

                    step.innerHTML = `
                        <strong>
                            Step ${stepNumber}: ${skill}
                        </strong>

                        <p>
                            ${recommendation}
                        </p>
                    `;


                    roadmap.appendChild(
                        step
                    );

                }
            );

        } else {

            roadmap.innerHTML =
                "<p>No learning roadmap required. Your current skills match the requirements.</p>";
        }
    }


    // ======================================
    // SHOW RESULTS
    // ======================================

    results.classList.remove(
        "hidden"
    );


    // ======================================
    // SMOOTH SCROLL
    // ======================================

    setTimeout(
        function () {

            results.scrollIntoView(
                {
                    behavior: "smooth",
                    block: "start"
                }
            );

        },
        200
    );

}