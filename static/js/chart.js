/*global $*/
/*global Chart*/
/*global console*/
$(document).ready(function () {
    var endpoint = "/graphs/graph_data/";
    var product_labels = [];
    var product_count = [];
    var suggestion_labels = [];
    var suggestion_count = [];
    var upvote_labels = [];
    var upvote_count = [];
    var view_labels = [];
    var view_count = [];
    $.ajax({
        method: "GET",
        url: endpoint,
        success: function (data) {
            product_labels = data.product_labels;
            product_count = data.product_count;

            suggestion_labels = data.suggestion_labels;
            suggestion_count = data.suggestion_count;

            upvote_labels = data.upvote_labels;
            upvote_count = data.upvote_count;

            view_labels = data.view_labels;
            view_count = data.view_count;

            var suggestionPieChart = $("#suggestionPieChart")[0].getContext("2d");
            suggestionPieChart = new Chart(suggestionPieChart, {
                type: "pie",
                data: {
                    labels: suggestion_labels,
                    datasets: [
                        {
                            data: suggestion_count,
                            backgroundColor: ["red", "gold", "green"]
                        }
                    ]
                },
                options: {
                    legend: {
                        display: true,
                        position: "top",
                        labels: {
                            fontColor: "#000000",
                            fontSize: 18
                        }
                    }
                }
            });

            var suggestionBarChart = $("#suggestionBarChart")[0].getContext("2d");
            suggestionBarChart = new Chart(suggestionBarChart, {
                type: "bar",
                data: {
                    labels: upvote_labels,
                    datasets: [{
                        label: "# of Votes",
                        data: upvote_count,
                        backgroundColor: [
                            "#002366",
                            "#660023",
                            "#430066",
                            "#b3003d",
                            "#f0352c"
                        ]
                    }]
                },
                options: {
                    legend: {
                        labels: {
                            fontColor: "#000000"
                        }
                    },
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true,
                                fontColor: "#000000"
                            }
                        }],
                        xAxes: [{
                            ticks: {
                                fontColor: "#000000"
                            }
                        }]
                    }
                }
            });

            var productBarChart = $("#productBarChart")[0].getContext("2d");
            productBarChart = new Chart(productBarChart, {
                type: "bar",
                data: {
                    labels: view_labels,
                    datasets: [{
                        label: "# of Views",
                        data: view_count,
                        backgroundColor: [
                            "#002366",
                            "#660023",
                            "#430066",
                            "#b3003d",
                            "#f0352c"
                        ]
                    }]
                },
                options: {
                    legend: {
                        labels: {
                            fontColor: "#000"
                        }
                    },
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true,
                                fontColor: "#000"
                            }
                        }],
                        xAxes: [{
                            ticks: {
                                fontColor: "#000"
                            }
                        }]
                    }
                }
            });
        },

        error: function (error_data) {
            console.log("error");
            console.log(error_data);
        }
    });
});