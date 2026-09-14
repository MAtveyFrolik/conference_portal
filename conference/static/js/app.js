document.addEventListener("DOMContentLoaded", () => {
    const navToggle = document.querySelector("[data-nav-toggle]");
    const nav = document.querySelector("[data-nav]");

    if (navToggle && nav) {
        navToggle.addEventListener("click", () => {
            nav.classList.toggle("is-open");
        });
    }

    const roomSelect = document.querySelector("[data-room-select]");
    const roomTiles = Array.from(document.querySelectorAll("[data-room-tile]"));

    function syncRoomPreview() {
        const value = roomSelect ? roomSelect.value : "";
        roomTiles.forEach((tile) => {
            tile.classList.toggle("is-active", tile.dataset.roomTile === value);
        });
    }

    if (roomSelect && roomTiles.length) {
        roomSelect.addEventListener("change", syncRoomPreview);
        syncRoomPreview();
    }

    document.querySelectorAll("[data-min-now]").forEach((field) => {
        const now = new Date();
        now.setMinutes(now.getMinutes() - now.getTimezoneOffset() + 5);
        field.min = now.toISOString().slice(0, 16);
    });

    document.querySelectorAll("[data-review-field]").forEach((field) => {
        const counter = field.closest(".field")?.querySelector("[data-review-count]");
        const updateCounter = () => {
            if (counter) {
                counter.textContent = `${field.value.length} / ${field.maxLength || 800}`;
            }
        };
        field.addEventListener("input", updateCounter);
        updateCounter();
    });

    const revealItems = document.querySelectorAll(".reveal");
    if ("IntersectionObserver" in window) {
        const observer = new IntersectionObserver(
            (entries) => {
                entries.forEach((entry) => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add("is-visible");
                        observer.unobserve(entry.target);
                    }
                });
            },
            { threshold: 0.08 }
        );
        revealItems.forEach((item) => observer.observe(item));
    } else {
        revealItems.forEach((item) => item.classList.add("is-visible"));
    }
});

