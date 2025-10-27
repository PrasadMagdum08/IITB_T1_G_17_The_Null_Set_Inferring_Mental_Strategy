fetch('/data')
    .then(response => response.json())
    .then(data => {
        const holisticData = {
            labels: data.holistic.map(p => p.participant_id),
            datasets: [{
                label: 'Fixation Mean',
                data: data.holistic.map(p => p.fixation_mean),
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgba(255, 99, 132, 1)',
                borderWidth: 1
            }, {
                label: 'Saccade Mean',
                data: data.holistic.map(p => p.saccade_mean),
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            }]
        };

        const piecemealData = {
            labels: data.piecemeal.map(p => p.participant_id),
            datasets: [{
                label: 'Fixation Mean',
                data: data.piecemeal.map(p => p.fixation_mean),
                backgroundColor: 'rgba(255, 206, 86, 0.2)',
                borderColor: 'rgba(255, 206, 86, 1)',
                borderWidth: 1
            }, {
                label: 'Saccade Mean',
                data: data.piecemeal.map(p => p.saccade_mean),
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        };

        const combinedData = {
            labels: ['Holistic', 'Piecemeal'],
            datasets: [{
                label: 'Number of Participants',
                data: [data.holistic.length, data.piecemeal.length],
                backgroundColor: ['rgba(255, 99, 132, 0.2)', 'rgba(54, 162, 235, 0.2)'],
                borderColor: ['rgba(255, 99, 132, 1)', 'rgba(54, 162, 235, 1)'],
                borderWidth: 1
            }]
        };

        const holisticChart = new Chart(document.getElementById('holisticChart'), {
            type: 'bar',
            data: holisticData,
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });

        const piecemealChart = new Chart(document.getElementById('piecemealChart'), {
            type: 'bar',
            data: piecemealData,
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });

        const combinedChart = new Chart(document.getElementById('combinedChart'), {
            type: 'pie',
            data: combinedData
        });
    });