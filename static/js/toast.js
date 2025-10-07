function showToast(title, message, type = 'normal', duration = 3000) {
    const toastComponent = document.getElementById('toast-component');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');
    
    if (!toastComponent) return;

    // Remove all type classes first
    toastComponent.classList.remove(
        'bg-red-50', 'border-red-500', 'text-red-600',
        'bg-green-50', 'border-green-500', 'text-green-600',
        'bg-white', 'border-gray-300', 'text-gray-800'
    );

    // Set type styles and icon
    if (type === 'success') {
        toastComponent.classList.add('bg-gray-50', 'border-gray-500', 'text-gray-900');
        toastComponent.style.border = '1px solid #64686eff'; // bluish-gray
    } else if (type === 'error') {
        toastComponent.classList.add('bg-gray-50', 'border-gray-500', 'text-[#b02a29]');
        toastComponent.style.border = '1px solid #b08f8fff'; // red tone
    } else {
        toastComponent.classList.add('bg-white', 'border-gray-300', 'text-gray-700');
        toastComponent.style.border = '1px solid #d1d5db'; // light gray
    }

    toastTitle.textContent = title;
    toastMessage.textContent = message;

    toastComponent.classList.remove('opacity-0', 'translate-y-64');
    toastComponent.classList.add('opacity-100', 'translate-y-0');

    setTimeout(() => {
        toastComponent.classList.remove('opacity-100', 'translate-y-0');
        toastComponent.classList.add('opacity-0', 'translate-y-64');
    }, duration);
}