"""Explicit precipitation units and regular-grid area weighting."""
import calendar
import numpy as np


def precipitation_mm(values, convention, year=None, month=None, seconds=None):
    """Convert without silently conflating monthly mean daily depth and total."""
    values = np.asarray(values, dtype=float)
    if convention == "accumulated_m":
        return values * 1000.0
    if convention == "monthly_mean_daily_m":
        if year is None or month is None:
            raise ValueError("A calendar year and month are required.")
        return values * 1000.0 * calendar.monthrange(int(year), int(month))[1]
    if convention == "rate_kg_m2_s":
        if seconds is None or not np.all(np.isfinite(np.asarray(seconds))) or np.any(np.asarray(seconds) <= 0):
            raise ValueError("Positive, verified interval lengths in seconds are required.")
        return values * np.asarray(seconds)
    raise ValueError("Choose accumulated_m, monthly_mean_daily_m, or rate_kg_m2_s from metadata.")


def latitude_weighted_mean(values, latitude, axis=-2):
    """Approximate area mean on a regular lon/lat grid, renormalizing for missing data."""
    array = np.asarray(values, dtype=float)
    latitude = np.asarray(latitude, dtype=float)
    if latitude.ndim != 1 or array.shape[axis] != len(latitude):
        raise ValueError("Latitude must match the latitude axis of a regular grid.")
    shape = [1] * array.ndim
    shape[axis] = len(latitude)
    weight = np.broadcast_to(np.cos(np.deg2rad(latitude)).reshape(shape), array.shape)
    valid = np.isfinite(array)
    denominator = np.sum(np.where(valid, weight, 0.0))
    return float(np.sum(np.where(valid, array * weight, 0.0)) / denominator) if denominator else float("nan")


def weighted_interval_mean(means, valid_counts):
    """Sample-weighted composite statistic; this is not a calendar-time mean."""
    means, counts = np.asarray(means, dtype=float), np.asarray(valid_counts, dtype=float)
    if means.shape != counts.shape or np.any(counts < 0):
        raise ValueError("Means and nonnegative counts must have identical shape.")
    valid = np.isfinite(means) & np.isfinite(counts) & (counts > 0)
    return float(np.average(means[valid], weights=counts[valid])) if np.any(valid) else float("nan")


def coordinate_slice(coordinate, low, high):
    """Handle ascending and descending xarray coordinates explicitly."""
    values = np.asarray(coordinate)
    if values.ndim != 1 or values.size < 2:
        raise ValueError("Expected a one-dimensional geographic coordinate.")
    if np.all(np.diff(values) > 0):
        return slice(low, high)
    if np.all(np.diff(values) < 0):
        return slice(high, low)
    raise ValueError("Coordinate is not monotonic; normalize/sort before selection.")
